from flask import Flask, render_template, request,session,redirect,url_for
import pandas as pd
import Jira_ticket_Flask as JT
from jira import JIRA
import os

api_token=os.environ.get('API')
counter=1
jiradf_backup=None
jira = JIRA(server='https://ticketingjiratool.atlassian.net/', basic_auth=('pythonlover976@gmail.com', api_token))
app=Flask("Jira Ticketing APP")
app.secret_key = 'viv1990'

@app.route('/status')
def status():
    error_message = request.args.get('status')
    return render_template('index.html', error_message=error_message)
def filevalidation(file):
    print(file)
    file_path = os.path.join(os.getcwd(), file.filename)
    if 'file' not in request.files:
        error_message = "Please select a file to upload"
        return redirect(url_for('status',status=error_message))
    if file.filename == '' or not file:
        error_message = "No file selected"
        return redirect(url_for('status', status=error_message))
        # return render_template('index.html', error_message=error_message)
    if file.filename != 'Jira.xlsx':
        error_message = "Invalid file name. Please upload 'Jira.xlsx'"
        return redirect(url_for('status', status=error_message))
    try:
        with open(file_path, 'r'):
            pass
    except PermissionError:
        return render_template('closefile.html')
@app.route('/', methods=['GET', 'POST'])
def index():
    session.clear()
    print("In Index")
    jiradf_backup=None
    df_list=[]
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            print(file)
            file_path = os.path.join(os.getcwd(), file.filename)
            print(file_path)
            if file:
                file.save(file_path)
            if 'execute_jira_status' in request.form:
                print('In execute jira status')
                error_template=filevalidation(file)
                print(error_template)
                if error_template:
                    return error_template
                else:
                    print("In for status execution")
                    status=JT.jirastatus(file)
                    return render_template('status.html', status=status)
            else:
                try:
                    error_template = filevalidation(file)
                    print(error_template)
                    if error_template:
                        return error_template
                    else:
                        messages, df1, df2 = JT.reload_dataframe(file)
                except FileNotFoundError:
                    error_message = "File not found"
                    return render_template('index.html', error_message=error_message)
                if len(messages)>0:
                    print(messages)
                    return render_template('index.html', messages=messages)
                else:
                    df1, df2 = JT.removeNull(df1, df2)
                    if df1 is not None:
                        if df2 is not None:
                            df_list.append(df1)
                            df_list.append(df2)
                        else:
                            df_list.append(df1)

                    other_sheet_df,jiradf_backup=JT.preserve(file,jiradf_backup)
                    master_df, merged_df_issue_list = JT.concatdf(df_list, other_sheet_df)
                    sheet_name = None
                    jiradf,sheet_name,filtered_list = JT.jirafile(file_path,master_df, merged_df_issue_list,jiradf_backup,other_sheet_df)
                    if jiradf is not None and len(filtered_list)!=0:
                        JT.jiraticket(sheet_name,jiradf, master_df,other_sheet_df,)
                        result = "Jira Tickets created successfully"
                    else:
                        result = "All the weekly issues already have tickets, so no new tickets required"
                    return render_template('results.html', result=result)
        else:
            error_message = "Please select a file to upload"
            return render_template('index.html', error_message=error_message)
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
