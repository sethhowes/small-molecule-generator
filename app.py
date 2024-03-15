from transformers import pipeline
from pydantic import BaseModel
import requests
from fastapi import FastAPI
from ray import serve

app = FastAPI()


# Request and repsonse types
class GeneratorRequest(BaseModel):
    selfies_sequence: str
    target_location: str

class GeneratorResponse(BaseModel):
    selfies_sequence:str



@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})
@serve.ingress(app)
class ChemGPT:
    def __init__(self):
        # Load model
        self.model = pipeline("text-generation", model="ncfrey/ChemGPT-4.7M")

    @app.post("/")
    def generate_selfie(self, request: GeneratorRequest) -> GeneratorResponse:
        # Run the model
        model_output = self.model(request.selfies_sequence)

        # Process the returned result
        sequence = model_output[0]["generated_text"] 

        return {"selfies_sequence": sequence}


generator_app = ChemGPT.bind()
