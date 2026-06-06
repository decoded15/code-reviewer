def load_prompt_template():

    with open("prompts/review_prompt.txt", "r") as file:
        return file.read()
    
def build_review_prompt(
            code,
            review_type,
            language,
            functions,
            imports,
            long_functions,
            deep_nesting,
            retrieved_context,
            import_count
        ):

    template = load_prompt_template()

    prompt = template.format(
            review_type=review_type,
            language=language,
            functions=functions,
            imports=imports,
            long_functions=long_functions,
            deep_nesting=deep_nesting,
            import_count=import_count,
            code=code,
            retrieved_context=retrieved_context
        )

    return prompt