import sys
import os
import sys
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)



from core.recursive_loop import run_recursive


query = "How to write an essay step by step thinking process"
result = run_recursive(query)

for key, value in result.items():
    print(f"\n🔹 {key.upper()}:\n{value}")
