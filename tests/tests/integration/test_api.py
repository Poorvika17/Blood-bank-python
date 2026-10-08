import os

import requests


BASE_URL = "http://app:8080"


def test_health():
    response = requests.get(f"{BASE_URL}/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["postgres"] is True
    assert data["redis"] is True


def test_root():
    response = requests.get(f"{BASE_URL}/")

    assert response.status_code == 200

    data = response.json()

    assert data["service"] == "blood-bank"


def test_compatibility():
    response = requests.get(f"{BASE_URL}/compatibility/O-")

    assert response.status_code == 200

    data = response.json()

    assert data["group"] == "O-"
    assert "A+" in data["can_donate_to"]


def test_donors():
    response = requests.get(f"{BASE_URL}/donors")

    assert response.status_code == 200

    data = response.json()

    assert "donors" in data
    assert len(data["donors"]) > 0


def test_match():
    response = requests.get(f"{BASE_URL}/match/A+")

    assert response.status_code == 200

    data = response.json()

    assert data["recipient"] == "A+"
    assert "matches" in data
    assert "count" in data


def test_unknown_blood_group():
    response = requests.get(f"{BASE_URL}/compatibility/XYZ")

    assert response.status_code == 400