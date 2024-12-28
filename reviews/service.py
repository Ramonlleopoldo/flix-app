from reviews.repository import ReviewsRepository
import streamlit as st


class ReviewsService:

    def __init__(self):
        self.reviews_repository = ReviewsRepository()

    def get_reviews(self):
        return self.reviews_repository.get_reviews()

    def post_reviews(self, user_name, movie, rating, coments):
        review = dict(
            user_name=user_name,
            movie=movie,
            rating=rating,
            coments=coments
        )
        st.success(f'Avaliação de "{user_name}" realizada com sucesso.')
        return self.reviews_repository.post_reviews(review)
