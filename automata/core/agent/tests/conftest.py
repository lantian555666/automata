import pytest

from automata.configs.automata_agent_configs import (
    AgentConfigVersion,
    AutomataAgentConfig,
    AutomataInstructionPayload,
)
from automata.core.agent.automata_agent_builder import AutomataAgentBuilder
from automata.tool_management.tool_management_utils import build_llm_toolkits


@pytest.fixture
def automata_agent():
    tool_list = ["python_indexer"]
    mock_llm_toolkits = build_llm_toolkits(tool_list)

    instruction_payload = AutomataInstructionPayload()

    instructions = "Test instruction."

    config_name = AgentConfigVersion.DEFAULT
    agent_config = AutomataAgentConfig.load(config_name)

    agent = (
        AutomataAgentBuilder.from_config(agent_config)
        .with_instruction_payload(instruction_payload)
        .with_instructions(instructions)
        .with_llm_toolkits(mock_llm_toolkits)
        .build()
    )
    return agent


@pytest.fixture
def automata_agent_builder():
    config_name = AgentConfigVersion.DEFAULT
    agent_config = AutomataAgentConfig.load(config_name)
    agent_builder = AutomataAgentBuilder.from_config(agent_config)
    return agent_builder


@pytest.fixture
def automata_agent_with_dev_main_builder():
    config_name = AgentConfigVersion.AUTOMATA_MAIN_DEV
    agent_config = AutomataAgentConfig.load(config_name)
    agent_builder = AutomataAgentBuilder.from_config(agent_config)
    return agent_builder
