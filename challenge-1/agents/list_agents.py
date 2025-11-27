import asyncio
import os
from azure.identity.aio import AzureCliCredential
from azure.ai.projects.aio import AIProjectClient
from dotenv import load_dotenv

load_dotenv(override=True)

async def main():
    project_endpoint = os.environ.get("AI_FOUNDRY_PROJECT_ENDPOINT")
    
    async with AzureCliCredential() as credential:
        async with AIProjectClient(
            endpoint=project_endpoint,
            credential=credential
        ) as project_client:
            
            print("\n📋 Listing all agents in Azure AI Foundry:\n")
            agents = project_client.agents.list_agents()
            
            async for agent in agents:
                print(f"Name: {agent.name}")
                print(f"ID: {agent.id}")
                print("-" * 50)

if __name__ == "__main__":
    asyncio.run(main())
