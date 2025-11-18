# Token Benchmark

A benchmarking tool to compare token usage across different data serialization formats (JSON, TOON, and VSC) when sending prompts to OpenAI's API.

## Overview

This tool measures and compares how many tokens different data formats consume when processed by OpenAI models. It's useful for optimizing API costs and understanding which format is most token-efficient for your use case.

## Formats Tested

- **JSON**: Standard JSON format with indentation
- **TOON**: Human-readable, whitespace-based format
- **VSC**: Value-Separated Compact format (CSV-like with delimiters)

## Installation

1. Clone this repository

2. Install `uv` (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   uv pip install openai
   ```

## Configuration

**Important**: Before running the script, you must set your OpenAI API key on line 7:

```python
client = OpenAI(api_key="YOUR_API_KEY")
```

Replace `"YOUR_API_KEY"` with your actual OpenAI API key.

## Usage

Run the benchmark script:

```bash
python token_benchmark.py
```

The script will:
1. Send the same data in three different formats to OpenAI's API
2. Measure token usage for each format
3. Display a summary comparison

## Benchmark Results

Based on test data (Mars exploration robot profile with skills, experience, and projects):

| Format | Input Tokens | Output Tokens | Total Tokens |
|--------|--------------|---------------|--------------|
| JSON   | 158          | 116           | **274**      |
| TOON   | 93           | 123           | **216**      |
| VSC    | 77           | 80            | **157**      |

**Winner**: VSC format uses **43% fewer tokens** than JSON.

### Understanding the Results

When evaluating these benchmarks, it's crucial to compare not just token counts but also the **quality of outputs**:

#### Why Compare Outputs?

1. **Quality Validation**: Ensures all formats produce comparable quality responses - significant differences suggest the model may misinterpret certain formats
2. **Fair Comparison**: Verifies this is an apples-to-apples comparison where token efficiency is the only variable
3. **Information Preservation**: Confirms no format loses important data during encoding
4. **Model Understanding**: Shows whether the model parses and comprehends each format equally well

#### What to Look For:

- **Completeness**: Does each output include all key facts (name, role, skills, projects)?
- **Accuracy**: Are the details correct in each response?
- **Consistency**: Are responses similar in structure and content?
- **Quality**: Is one format noticeably better/worse at conveying information?

**Key Insight**: If outputs are comparable in quality and completeness, VSC's 43% token savings represents a clear efficiency win. However, if any format produces lower quality output, the token savings may not justify the trade-off.

## Customization

You can modify the test data in the script to benchmark your own use cases. The script uses `gpt-4o-mini` by default, but you can change the model on line 49.
