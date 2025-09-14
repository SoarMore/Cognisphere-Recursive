import json
import os

class ContextStore:
    def __init__(self, filename="memory/context.json"):
        self.filename = filename
        self.context = {}
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.context = json.load(f)
            except Exception:
                self.context = {}

    def _save(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.context, f, indent=2)
        except Exception as e:
            print(f"[ContextStore] Save error: {str(e)}")

    def set(self, key, value):
        self.context[key] = value
        self._save()

    def get(self, key, default=None):
        return self.context.get(key, default)

    def delete(self, key):
        if key in self.context:
            del self.context[key]
            self._save()

    def clear(self):
        self.context = {}
        self._save()

    def all(self):
        return self.context
