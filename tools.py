import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader as PDFLoader
from crewai_tools.tools.serper_dev_tool import SerperDevTool

search_tool = SerperDevTool()

class BloodTestReportTool:
    @staticmethod
    def read_data_tool(path='data/sample.pdf'):
        docs = PDFLoader(file_path=path).load()
        full_report = ""
        for data in docs:
            content = data.page_content.replace("\n\n", "\n")
            full_report += content + "\n"
        return full_report

class NutritionTool:
    @staticmethod
    def analyze_nutrition_tool(blood_report_data):
        processed_data = blood_report_data.replace("  ", " ")
        return "Nutrition analysis functionality to be implemented"

class ExerciseTool:
    @staticmethod
    def create_exercise_plan_tool(blood_report_data):
        return "Exercise planning functionality to be implemented"
