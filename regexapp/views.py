import re
from django.shortcuts import render

def regex_tool(request):
    matches = []
    error = None
    text = ''
    pattern = ''
    match_details = []
    
    if request.method == 'POST':
        text = request.POST.get('text', '')
        pattern = request.POST.get('pattern', '')
        
        if text and pattern:
            try:
                # Find all matches with their positions
                for match in re.finditer(pattern, text):
                    match_details.append({
                        'text': match.group(),
                        'start': match.start(),
                        'end': match.end()
                    })
                matches = [match['text'] for match in match_details]
            except re.error as e:
                error = f"Invalid regex pattern: {e}"
    
    return render(request, 'regex_tool.html', {
        'text': text,
        'pattern': pattern,
        'matches': matches,
        'match_details': match_details,
        'error': error
    })