
class ComponentError(Exception):
    pass

class AlreadyHasAParentError(ComponentError):
    pass

class DoesNotHaveAParentError(ComponentError):
    pass

class NotAComponentContainerError(ComponentError):
    pass

class Component(object):

    def __init__(self):
        self.parent = None

    def has_a(self, ctype):
        return False

    def get_all(self, ctype=None):
        return []

    def contains(self, component):
        return False

    def attach(self, parent):
        if self.parent:
            raise AlreadyHasAParentError()
        parent.__attach_child(self)
        self.parent = parent

    def detach(self):
        if not self.parent:
            raise DoesNotHaveAParentError()
        self.parent.__detach_child(self)
        self.parent = None

    def __attach_child(self, child):
        raise NotAComponentContainerError()

    def __detach_child(self, child):
        raise NotAComponentContainerError()

class ComponentContainer(Component):

    def __init__(self):
        self.components = []

    def has_a(self, ctype):
        for component in self.components:
            if isinstance(component, ctype):
                return True
            elif component.has_a(ctype):
                return True
        return False

    def get_all(self, ctype):
        if ctype:
            out = []
            for component in self.components:
                if isinstance(component, ctype):
                    out.append(component)
                else:
                    out.extend(component.get_all(c_type))
            return out
        else:
            return self.components

    def contains(self, component):
        for my_component in self.components:
            if my_component is component:
                return True
            elif my_component.contains(component):
                return True
        return False

    def __attach_child(self, component):
        self.components.append(arg)

    def __detach_child(self, child):
        self.components.remove(child)
