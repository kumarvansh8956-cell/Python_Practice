from docx import Document

# Open the document
doc = Document("MANN KUMAR.docx")

# Replace text in paragraphs
for paragraph in doc.paragraphs:
    paragraph.text = paragraph.text.replace(
        "MANN KUMAR",
        "Vansh Kumar"
    )

    paragraph.text = paragraph.text.replace(
        "9354262533",
        "8287900125"
    )

# Save as a new file
doc.save("Vansh.docx")

print("Document updated successfully!")