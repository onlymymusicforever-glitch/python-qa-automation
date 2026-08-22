import os

from dotenv import load_dotenv

# 1. Ler a variável ENV (se não existir, usar "qa" por defeito)
env = os.environ.get("ENV", "qa")

# 2. Construir o nome do ficheiro .env correspondente
env_file = f"config/{env}.env"

# 3. Mostrar qual ambiente está activo (útil para debug)
print(f"Ambiente activo: {env}")

load_dotenv(env_file)