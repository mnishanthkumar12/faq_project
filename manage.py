ok
hekllllo
jhiiiii 
removed

@app.get("/")
async def read_root():
    return {"H": "World"}
@app.get("/hello")
def abc():
    return "Hi nishanth commit success"

@app.get("/health")
async def alive():
    """Implement a helthyyy check endpoint to verify the status of all dependencies"""
    result = {
        "status": "ok",
        "dependencies": {
            "database": "ok",
            "external_service": "ok",
            "cache": "ok"
        }
    }
    return result
