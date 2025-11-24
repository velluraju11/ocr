import sys
import argparse
from src.core.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description="Ryha AI Builder CLI")
    parser.add_argument("idea", nargs="?", help="The software idea you want to build.")

    args = parser.parse_args()

    idea = args.idea
    if not idea:
        print("🤖 Ryha AI Builder")
        idea = input("What do you want to build today, Boss? ")

    engine = Orchestrator()
    engine.build_software(idea)

if __name__ == "__main__":
    main()
