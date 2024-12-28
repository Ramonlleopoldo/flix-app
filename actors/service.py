from actors.repository import ActorsRespository
import streamlit as st


class ActorsService:
    def __init__(self):
        self.actors_repository = ActorsRespository()

    def get_actors(self):
        return self.actors_repository.get_actors()

    def post_actors(self, name, nationality):
        name = name.strip().title()
        actor_list = self.actors_repository.get_actors()
        for actor in actor_list:
            if actor['name'] == name:
                st.error('Esse ator já existe')
                return None

        st.success("ator cadastrado com sucesso")
        return self.actors_repository.post_actors(name, nationality)

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
