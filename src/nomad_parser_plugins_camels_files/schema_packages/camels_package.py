from nomad.datamodel import Schema
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
    Filter,
    SectionProperties,
)
from nomad.datamodel.metainfo.basesections import (
    Measurement,
)
from nomad.metainfo import Datetime, Quantity, SchemaPackage, Section


m_package = SchemaPackage()


class CamelsMeasurement(Measurement, Schema):
    m_def = Section(
        a_eln=ELNAnnotation(
            properties=SectionProperties(
                visible=Filter(
                    exclude=['location', 'lab_id', 'description'],
                ),
                order=[
                    'name',
                    'datetime',
                    'end_time',
                    'session_name',
                    'measurement_tags',
                    'measurement_description',
                    'measurement_comments',
                    'protocol_description',
                    'protocol_overview',
                    'plan_name',
                    'camels_user',
                    'camels_file',
                ],
            )
        )
    )
    measurement_description = Quantity(
        type=str,
        description='Measurement description',
        a_eln=ELNAnnotation(
            component='RichTextEditQuantity',
            label='Measurement description',
        ),
    )
    protocol_description = Quantity(
        type=str,
        description='Protocol description',
        a_eln=ELNAnnotation(
            component='RichTextEditQuantity',
            label='Protocol description',
        ),
    )
    protocol_overview = Quantity(
        type=str,
        description='Protocol overview',
        a_eln=ELNAnnotation(
            component='RichTextEditQuantity',
            label='Protocol overview',
        ),
    )
    measurement_comments = Quantity(
        type=str,
        description='Measurement comments',
        a_eln=ELNAnnotation(
            component='RichTextEditQuantity',
            label='Measurement comments',
        ),
    )
    measurement_tags = Quantity(
        type=str,
        shape=['*'],
        description='Measurement tags',
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            label='Tags',
        ),
    )
    plan_name = Quantity(
        type=str,
        description='Plan name',
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            label='Plan name',
        ),
    )
    end_time = Quantity(
        type=Datetime,
        description='Measurement end time',
        a_eln=dict(component='DateTimeEditQuantity', label='Measurement end time'),
    )
    session_name = Quantity(
        type=str,
        description='Session name',
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            label='Session name',
        ),
    )
    camels_user = Quantity(
        type=str,
        description='CAMELS User',
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            label='CAMELS User',
        ),
    )
    camels_file = Quantity(
        type=str,
        description='CAMELS file reference',
        a_eln=dict(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor', label='camels file ref'),
    )
    camels_python_script = Quantity(
        type=str,
        description='CAMELS Python script reference',
    )


m_package.__init_metainfo__()