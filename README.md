# Lab 03: Text Chunking

## 🎯 Learning Objectives

By the end of this lab, you will be able to:
- Split text into smaller chunks using Python
- Understand chunk size and overlap concepts
- Create reusable chunking functions
- Apply chunking to real documents

## ⏰ Time Allocation (3 hours)

| Activity | Duration |
|----------|----------|
| 🎯 Lecture & Slides | 30 min |
| 📖 Tutorial Notebook | 60 min |
| ☕ Break | 15 min |
| ✍️ Exercise Notebook | 45 min |
| 📤 Submit & Auto-grade | 15 min |
| 💬 Q&A | 15 min |

## 📚 Key Concepts

### Why Chunking?

LLMs have **token limits** (e.g., 4096 tokens). Large documents must be split into smaller pieces.

```
Document (5000 tokens) → [Chunk1 (1000)] [Chunk2 (1000)] [Chunk3 (1000)]...
```

### Chunk Size vs Overlap

```
Text: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

Chunk Size = 10, No Overlap:
[ABCDEFGHIJ] [KLMNOPQRST] [UVWXYZ]

Chunk Size = 10, Overlap = 3:
[ABCDEFGHIJ] [HIJKLMNOPQ] [OPQRSTUVWX] [VWXYZ]
```

Overlap helps maintain context between chunks!

## 🏆 Grading

| Exercise | Points |
|----------|--------|
| Exercise 1: Split text by characters | 25 |
| Exercise 2: Create chunk function | 25 |
| Exercise 3: Chunk with overlap | 25 |
| Exercise 4: Chunk a document | 25 |
| **Total** | **100** |

---
**Course:** CSI403 - Full Stack Program Development  
**Lab:** 03 - Text Chunking
