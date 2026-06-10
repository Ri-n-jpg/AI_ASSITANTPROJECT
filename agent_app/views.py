from rest_framework.decorators import api_view
from rest_framework.response import Response
from .agent import process_query

@api_view(['POST'])
def ask_question(request):
    try:
        question = request.data.get("question")

        if not question:
            return Response(
                {"error": "Question is required"},
                status=400
            )

        answer = process_query(question)

        return Response({
            "question": question,
            "answer": answer
        })

    except Exception as e:
        return Response(
            {
                "error": str(e)
            },
            status=500
        )