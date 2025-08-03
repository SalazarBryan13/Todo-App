import os
import sqlite3
import sys

import pytest

from app import app

# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def clean_db():
    """Fixture to ensure clean database for tests"""
    # Remove existing database if it exists
    if os.path.exists("todos.db"):
        os.remove("todos.db")

    # Create fresh database
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    conn.commit()
    conn.close()
    yield
    # Clean up after test
    if os.path.exists("todos.db"):
        os.remove("todos.db")


def test_index_page(client, clean_db):
    """Test that the index page loads correctly"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mi Lista de Tareas" in response.data


def test_add_todo(client, clean_db):
    """Test adding a new todo"""
    response = client.post(
        "/add",
        data={"title": "Test Todo", "description": "Test Description"},
        follow_redirects=True,
    )
    assert response.status_code == 200


def test_api_todos(client, clean_db):
    """Test the API endpoint"""
    response = client.get("/api/todos")
    assert response.status_code == 200
    assert response.is_json


def test_toggle_todo(client, clean_db):
    """Test toggling a todo status"""
    # First add a todo
    client.post("/add", data={"title": "Test Todo"})

    # Then toggle it
    response = client.get("/toggle/1", follow_redirects=True)
    assert response.status_code == 200


def test_delete_todo(client, clean_db):
    """Test deleting a todo"""
    # First add a todo
    client.post("/add", data={"title": "Test Todo"})

    # Then delete it
    response = client.get("/delete/1", follow_redirects=True)
    assert response.status_code == 200


def test_empty_todos_page(client, clean_db):
    """Test that empty todos page shows correct message"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"No hay tareas pendientes" in response.data


def test_todo_with_description(client, clean_db):
    """Test adding a todo with description"""
    response = client.post(
        "/add",
        data={
            "title": "Test Todo with Description",
            "description": "This is a test description",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
