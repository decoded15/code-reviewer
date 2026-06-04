import ast

def check_syntax(code):

    try:
        ast.parse(code)
        return True, None

    except SyntaxError as error:
        return False, str(error)
    
def extract_functions(code):

    tree = ast.parse(code)

    functions = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return functions

def extract_imports(code):

    tree = ast.parse(code)

    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for alias in node.names:
                imports.append(alias.name)

    return imports