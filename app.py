import gradio as gr

def audio_to_visual(audio, prompt):
    if (audio):
        return prompt
    else:
        return 'No Audio'

with gr.Blocks() as demo:
    gr.HTML(
    """
        <div style='display:flex; justify-content:center; align-items:center; flex-direction:column'>
            <h1 style='font-size:60px;'>Direct Aux</h1>
            <h2 style='font-size:40px;'>Unleash Your Music's Visual Potential</h2>
        </div>
    """
    )
    audio_file = gr.Audio(type="filepath")
    prompt = gr.Textbox(label='Prompt')
    result = gr.Video(label='Result')
     
    b1 = gr.Button("Create Visual")
    b1.click(fn=audio_to_visual, inputs=[audio_file, prompt] , outputs=result)

demo.launch()
