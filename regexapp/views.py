import re
import signal
from django.shortcuts import render

REGEX_TIMEOUT = 5  # seconds


class RegexTimeout(Exception):
    pass


def _timeout_handler(signum, frame):
    raise RegexTimeout()


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
                compiled = re.compile(pattern)
                old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
                signal.alarm(REGEX_TIMEOUT)
                try:
                    for match in compiled.finditer(text):
                        match_details.append({
                            'text': match.group(),
                            'start': match.start(),
                            'end': match.end(),
                        })
                finally:
                    signal.alarm(0)
                    signal.signal(signal.SIGALRM, old_handler)
                matches = [m['text'] for m in match_details]
            except RegexTimeout:
                error = (
                    "Pattern took too long to evaluate. "
                    "It may be too complex or cause catastrophic backtracking."
                )
            except re.error as e:
                error = f"Invalid regex pattern: {e}"

    return render(request, 'regex_tool.html', {
        'text': text,
        'pattern': pattern,
        'matches': matches,
        'match_details': match_details,
        'error': error,
    })