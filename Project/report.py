from reportlab.pdfgen import canvas

def make_report(count):
    pdf=canvas.Canvas("report.pdf")
    pdf.setTitle("Parking report")
    pdf.drawString(100, 750, "Barrier detection report")
    pdf.drawString(100, 720, f"Detected objects: {count}")
    pdf.save()