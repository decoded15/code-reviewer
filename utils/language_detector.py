def detect_language(file_name):

    extension_map = {
        ".py": "Python",
        ".js": "JavaScript",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C",
        ".ts": "TypeScript"
    }

    for extension, language in extension_map.items():

        if file_name.endswith(extension):
            return language

    return "Unknown"