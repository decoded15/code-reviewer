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

def detect_long_functions(code, max_lines=20):

    tree = ast.parse(code)

    long_functions = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            function_length = node.end_lineno - node.lineno

            if function_length > max_lines:

                long_functions.append({
                    "name": node.name,
                    "lines": function_length
                })

    return long_functions

def detect_deep_nesting(code, max_depth=3):

    tree = ast.parse(code)

    deep_nesting = []

    def check_depth(node, depth=0):

        if depth > max_depth:

            deep_nesting.append(type(node).__name__)

        for child in ast.iter_child_nodes(node):
            check_depth(child, depth + 1)

    check_depth(tree)

    return deep_nesting

def detect_many_imports(code, max_imports=10):

    imports = extract_imports(code)

    if len(imports) > max_imports:
        return True, len(imports)

    return False, len(imports)