"""LLM Factory for creating different language model instances."""

import os
from typing import Any, Optional

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI


def create_llm(model_name: str, temperature: float = 0.7, **kwargs) -> Any:
    """
    Create an LLM instance based on model name.

    Supports:
    - OpenAI models (gpt-4, gpt-4-turbo, gpt-3.5-turbo, etc.)
    - Anthropic models (claude-3-opus, claude-3-sonnet, claude-3-haiku)
    - Local models via Ollama (ollama/model-name)

    Args:
        model_name: Name of the model or provider/model
        temperature: Temperature setting (0.0-1.0)
        **kwargs: Additional provider-specific arguments

    Returns:
        Configured LLM instance

    Examples:
        >>> llm = create_llm("gpt-4-turbo-preview")
        >>> llm = create_llm("claude-3-opus-20240229")
        >>> llm = create_llm("ollama/llama2")
    """
    # Normalize model name
    model_name = model_name.strip()

    # Detect provider from model name
    if model_name.startswith("gpt-") or model_name.startswith("o1-"):
        return _create_openai_llm(model_name, temperature, **kwargs)

    elif model_name.startswith("claude-"):
        return _create_anthropic_llm(model_name, temperature, **kwargs)

    elif model_name.startswith("ollama/"):
        return _create_ollama_llm(model_name, temperature, **kwargs)

    else:
        # Default to OpenAI
        print(f"⚠️ Unknown model format '{model_name}', defaulting to OpenAI")
        return _create_openai_llm(model_name, temperature, **kwargs)


def _create_openai_llm(model_name: str, temperature: float, **kwargs) -> ChatOpenAI:
    """Create OpenAI LLM instance."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment")

    # Map common aliases
    model_mapping = {
        "gpt-4": "gpt-4-turbo-preview",
        "gpt-4-turbo": "gpt-4-turbo-preview",
        "gpt-3.5": "gpt-3.5-turbo",
    }

    actual_model = model_mapping.get(model_name, model_name)

    return ChatOpenAI(
        model=actual_model,
        temperature=temperature,
        api_key=api_key,
        **kwargs,
    )


def _create_anthropic_llm(model_name: str, temperature: float, **kwargs) -> ChatAnthropic:
    """Create Anthropic LLM instance."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment")

    # Map common aliases
    model_mapping = {
        "claude-3-opus": "claude-3-opus-20240229",
        "claude-3-sonnet": "claude-3-sonnet-20240229",
        "claude-3-haiku": "claude-3-haiku-20240307",
        "claude-3.5-sonnet": "claude-3-5-sonnet-20241022",
    }

    actual_model = model_mapping.get(model_name, model_name)

    return ChatAnthropic(
        model=actual_model,
        temperature=temperature,
        api_key=api_key,
        **kwargs,
    )


def _create_ollama_llm(model_name: str, temperature: float, **kwargs):
    """Create Ollama LLM instance for local models."""
    try:
        from langchain_community.llms import Ollama
    except ImportError:
        raise ImportError(
            "Ollama support requires langchain-community. "
            "Install with: pip install langchain-community"
        )

    # Extract model name after "ollama/"
    actual_model = model_name.split("/", 1)[1]
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    return Ollama(
        model=actual_model,
        temperature=temperature,
        base_url=base_url,
        **kwargs,
    )


def estimate_cost(
    model_name: str,
    input_tokens: int,
    output_tokens: int,
) -> float:
    """
    Estimate cost for a model based on token usage.

    Args:
        model_name: Name of the model
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens

    Returns:
        Estimated cost in USD
    """
    # Pricing as of Nov 2025 (per 1K tokens)
    pricing = {
        # OpenAI
        "gpt-4-turbo-preview": {"input": 0.01, "output": 0.03},
        "gpt-4": {"input": 0.03, "output": 0.06},
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        # Anthropic
        "claude-3-opus-20240229": {"input": 0.015, "output": 0.075},
        "claude-3-sonnet-20240229": {"input": 0.003, "output": 0.015},
        "claude-3-haiku-20240307": {"input": 0.00025, "output": 0.00125},
        "claude-3-5-sonnet-20241022": {"input": 0.003, "output": 0.015},
        # Local models
        "ollama": {"input": 0.0, "output": 0.0},
    }

    # Find pricing for model
    if model_name.startswith("ollama/"):
        rates = pricing["ollama"]
    else:
        rates = pricing.get(model_name, {"input": 0.01, "output": 0.03})

    input_cost = (input_tokens / 1000) * rates["input"]
    output_cost = (output_tokens / 1000) * rates["output"]

    return input_cost + output_cost


def get_recommended_models() -> dict:
    """
    Get recommended model configurations for different use cases.

    Returns:
        Dictionary of use case -> model name
    """
    return {
        "creative_high_quality": "gpt-4-turbo-preview",  # Best quality, higher cost
        "creative_balanced": "claude-3-5-sonnet-20241022",  # Great quality, moderate cost
        "creative_fast": "gpt-3.5-turbo",  # Fast and cheap
        "validation": "claude-3-haiku-20240307",  # Fast and cheap for validation
        "local_free": "ollama/llama2",  # Free local option
    }
