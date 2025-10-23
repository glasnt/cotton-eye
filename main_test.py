import main

def test_simple_url():
    response = main.get_context("https://github.com/glasnt/cotton-eye")
    assert response["repo"] == "glasnt/cotton-eye"
    assert response["branch"] == "main"
    assert response["dir"].strip() == ""

def test_branched_url():
    response = main.get_context("https://github.com/glasnt/cotton-eye/tree/example")
    assert response["repo"] == "glasnt/cotton-eye"
    assert response["branch"] == "example"
    assert response["dir"].strip() == ""

def test_dir_url():
    response = main.get_context("https://github.com/glasnt/cotton-eye/tree/example/templates")
    assert response["repo"] == "glasnt/cotton-eye"
    assert response["branch"] == "example"
    assert response["dir"] == "templates"
