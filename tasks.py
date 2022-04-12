import pty
from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/ui.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage html", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/initialize_database.py", pty=True)


@task
def pylint(ctx):
    ctx.run("pylint src", pty=True)


@task
def autopep(ctx): 
    ctx.run("autopep8 --in-place --recursive src", pty=True)