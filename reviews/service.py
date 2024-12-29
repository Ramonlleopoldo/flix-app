from reviews.repository import ReviewsRepository
import streamlit as st


class ReviewsService:

    def __init__(self):
        self.reviews_repository = ReviewsRepository()

    def get_reviews(self):
        if 'review' in st.session_state:
            return st.session_state.review
        review = self.reviews_repository.get_reviews()
        st.session_state.review = review
        return review

    def post_reviews(self, user_name, movie, stars, coments):
        review = dict(
            user_name=user_name,
            movie=movie,
            stars=stars,
            coments=coments
        )
        st.success(f'Avaliação de "{user_name}" realizada com sucesso.')
        new_review = self.reviews_repository.post_reviews(review)
        st.session_state.review.append(new_review)
        return new_review
