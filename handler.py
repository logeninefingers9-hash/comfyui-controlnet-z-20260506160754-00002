import runpod

def handler(event):
    # Your ComfyUI processing logic here
    return {"status": "success"}

runpod.serverless.start({"handler": handler})
