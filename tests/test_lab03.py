"""
Lab 03: Text Chunking - Auto-grading Tests
"""

import pytest
import os
import nbformat

# Get paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOK_PATH = os.path.join(BASE_DIR, 'exercise', 'Lab03_Exercise.ipynb')


@pytest.fixture(scope="session")
def student_namespace():
    """Execute student notebook and return namespace with variables."""
    
    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    namespace = {'__name__': '__main__'}
    
    original_dir = os.getcwd()
    exercise_dir = os.path.join(BASE_DIR, 'exercise')
    os.chdir(exercise_dir)
    
    try:
        for cell in nb.cells:
            if cell.cell_type == 'code':
                if '# Quick check' in cell.source or '# Verification' in cell.source:
                    continue
                try:
                    exec(cell.source, namespace)
                except Exception as e:
                    print(f"Cell execution warning: {e}")
    finally:
        os.chdir(original_dir)
    
    return namespace


# ============== Exercise 1: Split Text by Characters (25 points) ==============

def test_ex1_chunks_exists(student_namespace):
    """Test that chunks variable exists"""
    assert 'chunks' in student_namespace, "Variable 'chunks' not found"


def test_ex1_chunks_is_list(student_namespace):
    """Test that chunks is a list"""
    assert isinstance(student_namespace.get('chunks'), list), "'chunks' should be a list"


def test_ex1_chunks_count(student_namespace):
    """Test that chunks has correct count"""
    chunks = student_namespace.get('chunks', [])
    assert len(chunks) == 5, f"Expected 5 chunks, got {len(chunks)}"


def test_ex1_chunks_content(student_namespace):
    """Test that chunks have correct content"""
    chunks = student_namespace.get('chunks', [])
    if len(chunks) >= 2:
        assert chunks[0] == "Rubella ca", f"First chunk should be 'Rubella ca', got '{chunks[0]}'"
        assert chunks[1] == "uses fever", f"Second chunk should be 'uses fever', got '{chunks[1]}'"


# ============== Exercise 2: Create Chunk Function (25 points) ==============

def test_ex2_create_chunks_exists(student_namespace):
    """Test that create_chunks function exists"""
    assert 'create_chunks' in student_namespace, "Function 'create_chunks' not found"


def test_ex2_create_chunks_callable(student_namespace):
    """Test that create_chunks is callable"""
    assert callable(student_namespace.get('create_chunks')), "'create_chunks' should be a function"


def test_ex2_create_chunks_works(student_namespace):
    """Test that create_chunks works correctly"""
    func = student_namespace.get('create_chunks')
    if func:
        result = func("ABCDEFGHIJ", 3)
        assert result == ["ABC", "DEF", "GHI", "J"], f"create_chunks('ABCDEFGHIJ', 3) should return ['ABC', 'DEF', 'GHI', 'J'], got {result}"


# ============== Exercise 3: Chunk with Overlap (25 points) ==============

def test_ex3_chunk_overlap_exists(student_namespace):
    """Test that chunk_overlap function exists"""
    assert 'chunk_overlap' in student_namespace, "Function 'chunk_overlap' not found"


def test_ex3_chunk_overlap_callable(student_namespace):
    """Test that chunk_overlap is callable"""
    assert callable(student_namespace.get('chunk_overlap')), "'chunk_overlap' should be a function"


def test_ex3_chunk_overlap_works(student_namespace):
    """Test that chunk_overlap works correctly"""
    func = student_namespace.get('chunk_overlap')
    if func:
        result = func("ABCDEFGHIJKLMNO", 6, 2)
        if result and len(result) >= 2:
            assert result[0] == "ABCDEF", f"First chunk should be 'ABCDEF', got '{result[0]}'"
            assert result[1] == "EFGHIJ", f"Second chunk should be 'EFGHIJ', got '{result[1]}'"


# ============== Exercise 4: Chunk a Document (25 points) ==============

def test_ex4_num_chunks_exists(student_namespace):
    """Test that num_chunks variable exists"""
    assert 'num_chunks' in student_namespace, "Variable 'num_chunks' not found"


def test_ex4_num_chunks_is_int(student_namespace):
    """Test that num_chunks is an integer"""
    assert isinstance(student_namespace.get('num_chunks'), int), "'num_chunks' should be an integer"


def test_ex4_first_chunk_exists(student_namespace):
    """Test that first_chunk variable exists"""
    assert 'first_chunk' in student_namespace, "Variable 'first_chunk' not found"


def test_ex4_first_chunk_is_string(student_namespace):
    """Test that first_chunk is a string"""
    assert isinstance(student_namespace.get('first_chunk'), str), "'first_chunk' should be a string"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
