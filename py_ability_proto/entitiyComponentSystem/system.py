"""
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from typing import Optional
from uuid import uuid4

from py_ability_proto.abilities.base_ability import BaseAbility
from py_ability_proto.actors.base_actor import Actor


class EntityComponentSystem:
    """
    Implements a ECS, where the object itself is the world context.
    """

    def __init__(self):
        self.actors: list[Actor] = []
        self.abilities: list[BaseAbility] = []

    def add(self, entitiy: Actor | BaseAbility) -> None:
        """
        Adds an entity into its container and sets the entities iuid.
        Currently only Actor, BaseAbility and child classes supported.
        """
        if isinstance(entitiy, Actor):
            self.actors.append(entitiy)
        elif isinstance(entitiy, BaseAbility):
            self.abilities.append(entitiy)
        else:
            raise NotImplementedError
        self.set_entity_uuid(entitiy)

    def set_entity_uuid(self, entitiy: Actor | BaseAbility) -> None:
        """
        Sets the uuid for a given entity.
        """
        entitiy.set_uuid(uuid4())

    def remove(self, entitiy: Actor | BaseAbility) -> None:
        """
        Removes an entity into its container and unsets the entities iuid.
        Currently only Actor, BaseAbility and child classes supported.
        """
        if isinstance(entitiy, Actor):
            self.actors.remove(entitiy)
        elif isinstance(entitiy, BaseAbility):
            self.abilities.remove(entitiy)
        else:
            raise NotImplementedError
        entitiy.set_uuid(id=None)

    def list_ids(self, entitytype: Optional[str] = None) -> None:
        """
        Lists current objects in container if entitytype is provided.
        Otherwise lilsts all entities in all containers.
        """
        if entitytype:
            try:
                entities = getattr(self, entitytype)
            except Exception as exc:
                raise exc
            for entity in entities:
                print(entity)
            return

        for attr in dir(self):
            value = getattr(self, attr)

            try:
                if (
                    isinstance(value, list) and
                    issubclass(object, value[0].__class__.__mro__) and
                    len(value) > 0
                ):
                    for entry in value:
                        print(entry)
            except TypeError:
                pass
