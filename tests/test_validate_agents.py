import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_agents import validate_agent


class ValidateAgentTests(unittest.TestCase):
    def test_valid_agent(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp) / "sample-agent"
            folder.mkdir()
            (folder / "instructions.md").write_text("# Sample\n", encoding="utf-8")
            (folder / "agent.json").write_text(json.dumps({
                "id": "sample-agent", "name": "Sample", "version": "0.1.0",
                "description": "Example", "instructions": "instructions.md"
            }), encoding="utf-8")
            self.assertEqual(validate_agent(folder), [])

    def test_missing_instructions_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp) / "sample-agent"
            folder.mkdir()
            (folder / "agent.json").write_text(json.dumps({
                "id": "sample-agent", "name": "Sample", "version": "0.1.0",
                "description": "Example", "instructions": "instructions.md"
            }), encoding="utf-8")
            self.assertTrue(validate_agent(folder))


if __name__ == "__main__":
    unittest.main()
