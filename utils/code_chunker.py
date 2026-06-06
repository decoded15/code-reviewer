import ast
#AST - Abstract Syntax Tree

def chunk_python_code(code):
    tree = ast.parse(code)

    chunks = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            start_line = node.lineno - 1
            end_line = node.end_lineno

            code_lines = code.splitlines()

            function_code = "/n".join(code_lines[start_line : end_line])

            chunks.append({
                "type":"function",
                "name":node.name,
                "code":function_code
            })
    return chunks
