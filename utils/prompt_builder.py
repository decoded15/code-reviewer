def load_prompt_template():

    with open("prompts/review_prompt.txt", "r") as file:
        return file.read()
    
def build_review_prompt(code, review_type, language):

    template = load_prompt_template()

    prompt = template.format(
        review_type=review_type,
        language=language,
        code=code
    )

    return prompt