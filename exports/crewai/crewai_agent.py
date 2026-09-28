from crewai import Agent
def create_agent():
    return Agent(role='GitChurnGuard', goal='Autonomous SaaS Customer Churn Early Warning, Usage Telemetry & ARR Retention Agent', backstory='Autonomous agent', verbose=True)
