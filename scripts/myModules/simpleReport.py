#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(str(additional_info).replace('\n','<br />\n'), styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line])

def main():
    generate_report('test.pdf', 'Der Titel', "Mein Ende \n auf der zeiten Zeile")


if __name__ == "__main__":
    main()