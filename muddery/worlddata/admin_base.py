from django.contrib import admin

from muddery.worlddata.form_base import *


# Register your models here.


class ClassCategoriesAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'desc')


class TypeclassesAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'path',
                    'category',
                    'desc')


class WorldRoomsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'typeclass',
                    'desc',
                    'position')


class WorldExitsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'typeclass',
                    'desc',
                    'location',
                    'destination',
                    'condition')


class ExitLocksAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'unlock_condition',
                    'unlock_verb',
                    'locked_desc',
                    'auto_unlock')


class WorldObjectsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'typeclass',
                    'desc',
                    'location',
                    'condition')


class ObjectCreatorsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'loot_verb',
                    'loot_condition')


class LootListAdmin(admin.ModelAdmin):
    list_display = ('provider',
                    'object',
                    'number',
                    'odds',
                    'quest',
                    'condition')


class CommonObjectsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'typeclass',
                    'desc',
                    'max_stack',
                    'unique')


class EquipmentTypesAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'desc')


class EquipmentPositionsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'desc')


class EquipmentsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'typeclass',
                    'desc',
                    'max_stack',
                    'unique',
                    'position',
                    'type',
                    'attack',
                    'defence')


class CharacterCareersAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'desc')


class CareersEquipmentsAdmin(admin.ModelAdmin):
    list_display = ('career',
                    'equipment')


class CharacterModelsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'level',
                    'max_exp',
                    'max_hp',
                    'max_mp',
                    'attack',
                    'defence',
                    'give_exp')


class WorldNPCAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'typeclass',
                    'desc',
                    'location',
                    'model',
                    'level',
                    'condition')


class CommonCharactersAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'typeclass',
                    'desc',
                    'model',
                    'level')


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'typeclass',
                    'desc',
                    'cd',
                    'passive',
                    'condition',
                    'function',
                    'effect')


class DefaultSkillsAdmin(admin.ModelAdmin):
    list_display = ('character',
                    'skill')


class QuestsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'name',
                    'typeclass',
                    'desc',
                    'condition')


class QuestObjectiveTypesAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'type_id',
                    'name',
                    'desc')


class QuestObjectivesAdmin(admin.ModelAdmin):
    list_display = ('quest',
                    'ordinal',
                    'type',
                    'object',
                    'number',
                    'desc')


class QuestDependencyTypesAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'type_id',
                    'name',
                    'desc')


class QuestDependenciesAdmin(admin.ModelAdmin):
    list_display = ('quest',
                    'dependency',
                    'type')


class EventDataAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'object',
                    'type',
                    'trigger',
                    'condition')


class DialoguesAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'condition',
                    'get_have_quest')
    def get_have_quest(self, obj):
        if obj.have_quest:
            return obj.have_quest.key
    form = DialoguesForm


class DialogueRelationsAdmin(admin.ModelAdmin):
    list_display = ('get_dialogue',
                    'get_next')
    def get_dialogue(self, obj):
        return obj.dialogue.key
    def get_next(self, obj):
        return obj.next.key
    form = DialogueRelationsForm


class DialogueSentencesAdmin(admin.ModelAdmin):
    list_display = ('get_dialogue',
                    'ordinal',
                    'speaker',
                    'content',
                    'action',
                    'get_provide_quest',
                    'get_complete_quest')
    def get_dialogue(self, obj):
        return obj.dialogue.key
    def get_provide_quest(self, obj):
        if obj.provide_quest:
            return obj.provide_quest.key
    def get_complete_quest(self, obj):
        if obj.complete_quest:
            return obj.complete_quest.key
    form = DialogueSentencesForm


class NPCDialoguesAdmin(admin.ModelAdmin):
    list_display = ('get_npc',
                    'get_dialogue',
                    'default')
    def get_npc(self, obj):
        return obj.npc.key
    def get_dialogue(self, obj):
        return obj.dialogue.key
    form = NPCDialoguesForm


class DialogueQuestDependencyAdmin(admin.ModelAdmin):
    list_display = ('get_dialogue',
                    'get_dependency',
                    'type')
    def get_dialogue(self, obj):
        return obj.dialogue.key
    def get_dependency(self, obj):
        return obj.dependency.key
    form = DialogueQuestDependencyForm


class EventMobsAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'mob',
                    'level',
                    'odds',
                    'desc')


class EventDialoguesAdmin(admin.ModelAdmin):
    list_display = ('key',
                    'dialogue',
                    'npc')
    form = EventDialoguesForm


class LocalizedStringsAdmin(admin.ModelAdmin):
    list_display = ('origin',
                    'local')