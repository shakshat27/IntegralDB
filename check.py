import os

# --- Paste your actual keys here for verification ---
actual_GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
actual_SUPABASE_URL = "https://YOUR_PROJECT.supabase.co"
actual_SUPABASE_KEY = "YOUR_SUPABASE_KEY"
# ----------------------------------------------------

# Get from environment
env_GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
env_SUPABASE_URL = os.environ.get("SUPABASE_URL")
env_SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Compare
def compare(var_name, env_val, actual_val):
    if env_val is None:
        print(f"[❌] {var_name} not found in environment variables.")
    elif env_val == actual_val:
        print(f"[✅] {var_name} matches.")
    else:
        print(f"[⚠️] {var_name} does NOT match.")
        print(f"     Expected: {actual_val}")
        print(f"     Got:      {env_val}")

print("\n--- Environment Variable Verification ---\n")
compare("GOOGLE_API_KEY", env_GOOGLE_API_KEY, actual_GOOGLE_API_KEY)
compare("SUPABASE_URL", env_SUPABASE_URL, actual_SUPABASE_URL)
compare("SUPABASE_KEY", env_SUPABASE_KEY, actual_SUPABASE_KEY)
print("\n------------------------------------------\n")
