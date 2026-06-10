from rest_framework.decorators import api_view
from rest_framework.response import Response
from .agent import process_query
from .models import ChatHistory


@api_view(['POST'])
def ask_question(request):
    try:
        question = request.data.get("question")

        if not question:
            return Response({"error": "Question is required"}, status=400)

        # STEP 1: get answer
        answer = process_query(question)

        # STEP 2: SAVE TO DB (this is what you are missing or misplaced)
        ChatHistory.objects.create(
            question=question,
            answer=str(answer)
        )

        # STEP 3: return response
        return Response({
            "question": question,
            "answer": answer
        })

    except Exception as e:
        return Response({"error": str(e)}, status=500)