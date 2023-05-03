curl -X POST "http://localhost:8000/users/auth" \
    -H 'Content-Type: application/json' \
    -d '{"username": "user_01", "password": "a1234567"}'

printf "\n"

# --------------------------------------------
# Check the main file for the correct password *
# ---------------------------------------------