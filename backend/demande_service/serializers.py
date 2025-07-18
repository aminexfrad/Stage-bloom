"""
© 2025 Mohamed Amine FRAD. All rights reserved.
Unauthorized use, reproduction, or modification of this code is strictly prohibited.
Intellectual Property – Protected by international copyright law.
"""

from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from shared.security import SecurityValidator
from shared.utils import FileUploadValidator
from .models import Demande


class DemandeSerializer(serializers.ModelSerializer):
    """Serializer for demande de stage"""
    cv = serializers.FileField(required=False, allow_null=True)
    lettre_motivation = serializers.FileField(required=False, allow_null=True)
    demande_stage = serializers.FileField(required=False, allow_null=True)
    cv_binome = serializers.FileField(required=False, allow_null=True)
    lettre_motivation_binome = serializers.FileField(required=False, allow_null=True)
    demande_stage_binome = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Demande
        fields = [
            'id', 'nom', 'prenom', 'email', 'telephone', 'cin',
            'institut', 'specialite', 'type_stage', 'niveau', 'pfe_reference',
            'date_debut', 'date_fin', 'stage_binome',
            'nom_binome', 'prenom_binome', 'email_binome',
            'telephone_binome', 'cin_binome',
            'cv', 'lettre_motivation', 'demande_stage',
            'cv_binome', 'lettre_motivation_binome', 'demande_stage_binome',
            'status', 'raison_refus', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'status', 'raison_refus', 'created_at', 'updated_at']
    
    def validate_nom(self, value):
        """Validate and sanitize nom field"""
        try:
            return SecurityValidator.validate_name(value, "nom")
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
    
    def validate_prenom(self, value):
        """Validate and sanitize prenom field"""
        try:
            return SecurityValidator.validate_name(value, "prénom")
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
    
    def validate_email(self, value):
        """Validate and sanitize email field"""
        try:
            return SecurityValidator.validate_email(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
    
    def validate_telephone(self, value):
        """Validate and sanitize telephone field"""
        try:
            return SecurityValidator.validate_phone(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
    
    def validate_cin(self, value):
        """Validate and sanitize CIN field"""
        if value:
            try:
                return SecurityValidator.validate_text(value, max_length=20, allow_html=False)
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
        return value
    
    def validate_institut(self, value):
        """Validate and sanitize institut field"""
        try:
            return SecurityValidator.validate_text(value, max_length=200, allow_html=False)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
    
    def validate_specialite(self, value):
        """Validate and sanitize specialite field"""
        try:
            return SecurityValidator.validate_text(value, max_length=200, allow_html=False)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
    
    def validate_pfe_reference(self, value):
        """Validate and sanitize PFE reference field"""
        if value:
            try:
                return SecurityValidator.validate_text(value, max_length=100, allow_html=False)
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
        return value
    
    def validate_nom_binome(self, value):
        """Validate and sanitize nom_binome field"""
        if value:
            try:
                return SecurityValidator.validate_name(value, "nom du binôme")
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
        return value
    
    def validate_prenom_binome(self, value):
        """Validate and sanitize prenom_binome field"""
        if value:
            try:
                return SecurityValidator.validate_name(value, "prénom du binôme")
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
        return value
    
    def validate_email_binome(self, value):
        """Validate and sanitize email_binome field"""
        if value:
            try:
                return SecurityValidator.validate_email(value)
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
        return value
    
    def validate_telephone_binome(self, value):
        """Validate and sanitize telephone_binome field"""
        if value:
            try:
                return SecurityValidator.validate_phone(value)
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
        return value
    
    def validate_cin_binome(self, value):
        """Validate and sanitize cin_binome field"""
        if value:
            try:
                return SecurityValidator.validate_text(value, max_length=20, allow_html=False)
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
        return value
    
    def validate_file_field(self, value, field_name):
        """Generic file validation for PDF files only"""
        if value:
            # Validate file size and type
            allowed_types = ['application/pdf']
            max_size = 10 * 1024 * 1024  # 10MB
            
            try:
                FileUploadValidator.validate_file(value, allowed_types, max_size)
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
            
            # Validate filename safety
            if not FileUploadValidator.is_safe_filename(value.name):
                raise serializers.ValidationError(
                    f'Le nom du fichier {field_name} contient des caractères dangereux.'
                )
        
        return value
    
    def validate_cv(self, value):
        """Validate CV file"""
        return self.validate_file_field(value, 'CV')
    
    def validate_lettre_motivation(self, value):
        """Validate lettre de motivation file"""
        return self.validate_file_field(value, 'lettre de motivation')
    
    def validate_demande_stage(self, value):
        """Validate demande stage file"""
        return self.validate_file_field(value, 'demande de stage')
    
    def validate_cv_binome(self, value):
        """Validate binôme CV file"""
        return self.validate_file_field(value, 'CV binôme')
    
    def validate_lettre_motivation_binome(self, value):
        """Validate binôme lettre de motivation file"""
        return self.validate_file_field(value, 'lettre de motivation binôme')
    
    def validate_demande_stage_binome(self, value):
        """Validate binôme demande stage file"""
        return self.validate_file_field(value, 'demande de stage binôme')
    
    def validate(self, data):
        """Validate demande data"""
        # Check if stage dates are valid
        if data.get('date_debut') and data.get('date_fin'):
            if data['date_debut'] >= data['date_fin']:
                raise serializers.ValidationError(
                    'La date de fin doit être postérieure à la date de début.'
                )
        
        # Validate PFE reference for PFE stages
        if data.get('type_stage') in ['Stage PFE', 'Stage de Fin d\'Études']:
            if not data.get('pfe_reference'):
                raise serializers.ValidationError(
                    'La référence du projet PFE est obligatoire pour les stages PFE.'
                )
        
        # Validate binôme data if stage_binome is True
        if data.get('stage_binome'):
            required_binome_fields = ['nom_binome', 'prenom_binome', 'email_binome']
            for field in required_binome_fields:
                if not data.get(field):
                    raise serializers.ValidationError(
                        f'Le champ {field} est requis pour un stage en binôme.'
                    )
        
        return data


class DemandeListSerializer(DemandeSerializer):
    """Serializer for listing demandes (RH view)"""
    
    nom_complet = serializers.CharField(read_only=True)
    nom_complet_binome = serializers.CharField(read_only=True)
    duree_stage = serializers.IntegerField(read_only=True)
    is_pfe_stage = serializers.BooleanField(read_only=True)
    
    class Meta(DemandeSerializer.Meta):
        fields = [
            'id', 'nom_complet', 'email', 'institut', 'specialite',
            'type_stage', 'niveau', 'pfe_reference', 'date_debut', 'date_fin',
            'duree_stage', 'stage_binome', 'nom_complet_binome',
            'is_pfe_stage', 'status', 'created_at',
            'cv', 'lettre_motivation', 'demande_stage',
            'cv_binome', 'lettre_motivation_binome', 'demande_stage_binome',
        ]


class DemandeDetailSerializer(DemandeSerializer):
    """Serializer for detailed demande view"""
    
    nom_complet = serializers.CharField(read_only=True)
    nom_complet_binome = serializers.CharField(read_only=True)
    duree_stage = serializers.IntegerField(read_only=True)
    is_pfe_stage = serializers.BooleanField(read_only=True)
    
    class Meta(DemandeSerializer.Meta):
        fields = DemandeSerializer.Meta.fields + [
            'nom_complet', 'nom_complet_binome', 'duree_stage', 'is_pfe_stage'
        ]


class DemandeApprovalSerializer(serializers.Serializer):
    """Serializer for approving/rejecting demandes"""
    action = serializers.ChoiceField(choices=['approve', 'reject'])
    raison = serializers.CharField(required=False, allow_blank=True)
    
    def validate_action(self, value):
        if value not in ['approve', 'reject']:
            raise serializers.ValidationError(
                'L\'action doit être "approve" ou "reject".'
            )
        return value
    
    def validate_raison(self, value):
        """Validate and sanitize raison field"""
        if value:
            try:
                return SecurityValidator.validate_text(value, max_length=500, allow_html=False)
            except ValidationError as e:
                raise serializers.ValidationError(str(e))
        return value
    
    def validate(self, data):
        if data.get('action') == 'reject' and not data.get('raison'):
            raise serializers.ValidationError(
                'Une raison est requise pour rejeter une demande.'
            )
        return data 