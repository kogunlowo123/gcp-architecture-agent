"""Test configuration for GCP Architecture Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "gcp-architecture-agent", "category": "Cloud Engineering"}
