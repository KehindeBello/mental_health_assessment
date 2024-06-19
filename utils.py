from questions_mappings import questions, gad7_mapping, phq9_mapping, pss4_mapping

def calculate_scores(phq9scores, gad7scores, pss4scores):
    phq9_normalized = sum(phq9scores) / 27
    gad7_normalized = sum(gad7scores) / 21
    pss4_normalized = sum(pss4scores) / 16
    aggregate_score = (phq9_normalized + gad7_normalized + pss4_normalized) / 3
    return phq9_normalized, gad7_normalized, pss4_normalized, aggregate_score

def interpret_results(phq9scores, phq9_normalized, gad7_normalized, pss4_normalized, aggregate_score):
    category = {
        "Minimal concerns": "This individual is generally functioning well in their daily life without significant distress or impairment.",
        "Mild concerns": "This individual may have mild symptoms of anxiety, depression, or stress. These symptoms might cause some discomfort but do not significantly impair daily functioning.",
        "Moderate concerns": "The individual is likely experiencing moderate symptoms that may affect their daily life and well-being. These symptoms could interfere with work, relationships, and leisure activities.",
        "Moderately severe concerns": "The individual has significant symptoms that are likely causing considerable distress and impairing daily functioning. This level of concern often indicates that symptoms are affecting multiple areas of life.",
        "Severe concerns": "The individual has significant symptoms that are likely causing considerable distress and impairing daily functioning. This level of concern often indicates that symptoms are affecting multiple areas of life."
    }

    if phq9scores[-1] > 0:
        for key in category:
            category[key] += " Individual needs further assessment for suicide risk by someone who is competent to assess this risk."

    if aggregate_score <= 0.19:
        result = "Minimal concerns"
    elif aggregate_score <= 0.39:
        result = "Mild concerns"
    elif aggregate_score <= 0.59:
        result = "Moderate concerns"
    elif aggregate_score <= 0.79:
        result = "Moderately severe concerns"
    else:
        result = "Severe concerns"

    return result, category[result]


def collect_response(request):
    form_data = request.form.to_dict()
    mapped_response = []
    for question, response in form_data.items():
        if question.startswith('phq9_'):
            question_text = questions[question]
            response_text = phq9_mapping[response]
        elif question.startswith('gad7_'):
            question_text = questions[question]
            response_text = gad7_mapping[response]
        elif question.startswith('pss_'):
            question_text = questions[question]
            response_text = pss4_mapping[response]
        else:
            continue

        mapped_response.append({
            'question': question_text,
            'response': response_text
        })
    
    return mapped_response
