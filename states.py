from pydantic import BaseModel,Field,ConfigDict
from typing import Optional
class File(BaseModel):
    path : str =Field(description='the path of the file')
    purpose : str = Field(description='The purpose of the file. eg - main application logic, data processing module etc')



class Plan(BaseModel):
    name : str = Field(description='The name of the application to be built')
    description : str =Field(description='the description of the application to be built. Eg - A web application for managing the people working in a company')
    techstack : str=Field(description='The teck stack used for the application. Eg - Python, Streamlit, javascript, Flast, FastAPI etc')
    features : list[str] = Field (description='A list of features that the app should have. eg - user authentication, data vizualization, Leave Planner etc')
    files : list[File] = Field(description='A list of files to be created , each with a path and a purpose')
    
class ImplementationTask(BaseModel):
    filepath:str=Field(description='The path to the file to be modified')
    task_description : str=Field(description='A detailed description of the task to be performed on the file . Eg - add user authentication, implement data processing logic etc ')

class TaskPlan(BaseModel):
    implementation_steps:list[ImplementationTask]=Field(description='A list of steps to be taken to implement the task.')
    model_config=ConfigDict(extra='allow')

class CoderState(BaseModel):
    task_plan: TaskPlan = Field(description="The plan for the task to be implemented")
    current_step_idx: int = Field(0, description="The index of the current step in the implementation steps")
    current_file_content: Optional[str] = Field(None, description="The content of the file currently being edited or created")