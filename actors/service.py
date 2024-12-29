from actors.repository import ActorsRespository
import streamlit as st


class ActorsService:
    def __init__(self):
        self.actors_repository = ActorsRespository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.actors_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def post_actors(self, name, nationality):
        name = name.strip().title()
        actor_list = self.actors_repository.get_actors()
        for actor in actor_list:
            if actor['name'] == name:
                st.error('Esse ator já existe')
                return None

        st.success("ator cadastrado com sucesso")
        new_actor = self.actors_repository.post_actors(name, nationality)
        st.session_state.actors.append(new_actor)
        return new_actor

    def update_actors(self, id, name, nationality):
        name = name.strip().title()
        actor_list = self.actors_repository.get_actors()
        for actor in actor_list:
            if actor['name'] == name:
                st.error('Esse ator já existe')
                return None
        st.success("Ator atualizado com sucesso")
        return self.actors_repository.update_actor(id, name, nationality)

    def delete_actor(self, id):
        st.success("Ator deletado com sucesso")
        return self.actors_repository.delete_actor(id)
