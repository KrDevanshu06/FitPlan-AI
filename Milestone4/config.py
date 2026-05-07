"""
config.py — Centralized environment configuration for FitPlan Pro.

This module loads and validates all environment variables in one place.
Provides clear error messages if required configs are missing.
"""

import os
from dotenv import load_dotenv

# ── Load environment variables from .env file ─────────────────────────────────
load_dotenv()


# ══════════════════════════════════════════════════════════════════════════════
# Supabase Configuration
# ══════════════════════════════════════════════════════════════════════════════
SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "").strip()
SUPABASE_ENABLED = bool(SUPABASE_URL and SUPABASE_KEY)

if not SUPABASE_ENABLED:
    print("⚠️  WARNING: Supabase not configured. Using SQLite fallback.")
    print("   Setup Supabase: https://supabase.com (free forever)")
    print("   Then add SUPABASE_URL and SUPABASE_KEY to .env file")


# ══════════════════════════════════════════════════════════════════════════════
# Groq API Configuration
# ══════════════════════════════════════════════════════════════════════════════
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
GROQ_ENABLED = bool(GROQ_API_KEY)

if not GROQ_ENABLED:
    print("⚠️  WARNING: Groq API key not set. AI plan generation will fail.")
    print("   Setup: https://console.groq.com")
    print("   Then add GROQ_API_KEY to .env file")


# ══════════════════════════════════════════════════════════════════════════════
# Brevo (Email) Configuration
# ══════════════════════════════════════════════════════════════════════════════
BREVO_API_KEY = os.getenv("BREVO_API_KEY", "").strip()
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "").strip()
BREVO_ENABLED = bool(BREVO_API_KEY and EMAIL_SENDER)

if not BREVO_ENABLED:
    print("⚠️  WARNING: Email service (Brevo) not configured.")
    print("   Signup verification will not work.")
    print("   Setup: https://www.brevo.com")
    print("   Then add BREVO_API_KEY and EMAIL_SENDER to .env file")


# ══════════════════════════════════════════════════════════════════════════════
# Other Configuration
# ══════════════════════════════════════════════════════════════════════════════
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN", "").strip()


# ══════════════════════════════════════════════════════════════════════════════
# Configuration Summary (for debugging)
# ══════════════════════════════════════════════════════════════════════════════
def print_config_status():
    """Print configuration status for debugging."""
    print("\n" + "=" * 80)
    print("FitPlan Pro Configuration Status")
    print("=" * 80)
    print(f"✓ Supabase:      {'ENABLED' if SUPABASE_ENABLED else 'DISABLED (fallback: SQLite)'}")
    print(f"✓ Groq API:      {'ENABLED' if GROQ_ENABLED else 'DISABLED'}")
    print(f"✓ Email (Brevo): {'ENABLED' if BREVO_ENABLED else 'DISABLED'}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    print_config_status()
