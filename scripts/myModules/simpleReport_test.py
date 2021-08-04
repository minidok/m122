#!/usr/bin/env python3
import unittest
from unittest.case import TestCase
import simpleReport
import os

class TestsimpleReportClass(unittest.TestCase):
    def test_Generate(self):
        reportFileName = 'test.pdf'
        simpleReport.generate_report(reportFileName, 'Der Titel', "Mein Ende \n auf der zeiten Zeile")
        #rf = open(reportFileName, "rb") 
        file_size =os.stat(reportFileName).st_size
        #rf.close
        self.assertEqual(file_size, 1660, "filesize must be 1660 bytes")

if __name__ =='__main__':
    unittest.main()