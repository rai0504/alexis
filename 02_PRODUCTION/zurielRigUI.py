import bpy

### Rig Controls
class RigUI(bpy.types.Panel):
    bl_label = "Rig Controls"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "posemode"
    
    def draw(self, context):
        if context.active_object.type == 'NoneType':
            return
        layout = self.layout
        row = layout.row()
        pose_bones = context.active_object.pose.bones
        try:
            selected_bones = [bone.name for bone in context.selected_pose_bones]
            selected_bones += [context.active_pose_bone.name]
        except (AttributeError, TypeError):
            return
        
        def isSelected(names):
        # returns whether any of the named bones are selected
            if type(names) == list:
                for name in names:
                    if name in selected_bones:
                        return True
            elif names in selected_bones:
                return True
            return False
        
        # define the names to use for the bones and define what controls to 
        # show depending on the bones selected
        root = "root"
        
        # head and torso
        head = "head"
        neck = "neck"
        head_group = [head, neck]
        if isSelected(head_group):
            layout.prop(pose_bones["head"], '["isolate rotation"]', slider=True)
        
        chest = "chest"
        spine = "spine"
        hips = "hips"
        body = "body"
        torso_group = [chest, spine, hips, body]
        if isSelected(torso_group):
            layout.prop(pose_bones["body"], '["pivot"]', slider=True)
        
        # left arm    
        shoulderl = "shoulder.L"
        uprarmfkl = "upperarm.fk.L"
        forearmfkl = "forearm.fk.L"
        handfkl = "hand.fk.L"
        armfkl_group = [shoulderl, uprarmfkl, forearmfkl, handfkl]
        if isSelected(armfkl_group):
            layout.prop(pose_bones["MCH-upperarm.fk_par.L"], '["isolate rotation"]', slider=True)
            
        elbowpoleikl = "elbow.target.L"
        handikl = "hand.ik.L"
        armikl_group = [elbowpoleikl, handikl]
        arml_group = [elbowpoleikl, handikl, shoulderl, uprarmfkl, forearmfkl, handfkl]
        if isSelected(arml_group):
            layout.prop(pose_bones["hand.ik.L"], '["fk_ik"]', slider=True)
            
        #right arm
        shoulderr = "shoulder.R"
        uprarmfkr = "upperarm.fk.R"
        forearmfkr = "forearm.fk.R"
        handfkr = "hand.fk.R"
        armfkr_group = [shoulderr, uprarmfkr, forearmfkr, handfkr]
        if isSelected(armfkr_group):
            layout.prop(pose_bones["MCH-upperarm.fk_par.R"], '["isolate rotation"]', slider=True)
            
        elbowpoleikr = "elbow.target.R"
        handikr = "hand.ik.R"
        armikr_group = [elbowpoleikr, handikr]
        armr_group = [elbowpoleikr, handikr, shoulderr, uprarmfkr, forearmfkr, handfkr]
        if isSelected(armr_group):
            layout.prop(pose_bones["hand.ik.R"], '["fk_ik"]', slider=True)
        
        # left leg
        thighfkl = "thigh.fk.L"
        shinfkl = "shin.fk.L"
        footfkl = "foot.fk.L"
        toefkl = "toe.fk.L"
        legfkl_group = [thighfkl, shinfkl, footfkl, toefkl]
        if isSelected(legfkl_group):
            layout.prop(pose_bones["thigh.fk.L"], '["isolate rotation"]', slider=True)
            
        kneepolel = "knee.target.L"
        footikl = "foot.ik.L"
        toeikl = "toe.ik.L"
        footrollikl = "foot_roll.L"
        legikl_group = [kneepolel, footikl, toeikl, footrollikl]
        legl_group = [kneepolel, footikl, toeikl, footrollikl, thighfkl, shinfkl, footfkl, toefkl]
        if isSelected(legl_group):
            layout.prop(pose_bones["foot.ik.L"], '["fk_ik"]', slider=True)
        
        # right leg
        thighfkr = "thigh.fk.R"
        shinfkr = "shin.fk.R"
        footfkr = "foot.fk.R"
        toefkr = "toe.fk.R"
        legfkr_group = [thighfkr, shinfkr, footfkr, toefkr]
        if isSelected(legfkr_group):
            layout.prop(pose_bones["thigh.fk.R"], '["isolate rotation"]', slider=True)
            
        kneepoler = "knee.target.R"
        footikr = "foot.ik.R"
        toeikr = "toe.ik.R"
        footrollikr = "foot_roll.R"
        legikr_group = [kneepoler, footikr, toeikr, footrollikr]
        legr_group = [kneepoler, footikr, toeikr, footrollikr, thighfkr, shinfkr, footfkr, toefkr]
        if isSelected(legr_group):
            layout.prop(pose_bones["foot.ik.R"], '["fk_ik"]', slider=True)

        # fingers
        thumbfkl = "finger.thumb.fk.L"
        thumb2fkl = "finger.thumb2.fk.L"
        thumb3fkl = "finger.thumb3.fk.L"
        thumbikl = "finger.thumb.ik.L"
        thumbl_group = [thumbfkl, thumb2fkl, thumb3fkl, thumbikl]
        if isSelected(thumbl_group):
            layout.prop(pose_bones["finger.thumb.ik.L"], '["thumb.L fk_ik"]', slider=True)

        thumbfkr = "finger.thumb.fk.R"
        thumb2fkr = "finger.thumb2.fk.R"
        thumb3fkr = "finger.thumb3.fk.R"
        thumbikr = "finger.thumb.ik.R"
        thumbr_group = [thumbfkr, thumb2fkr, thumb3fkr, thumbikr]
        if isSelected(thumbr_group):
            layout.prop(pose_bones["finger.thumb.ik.R"], '["thumb.R fk_ik"]', slider=True)

        pointerfkl = "finger.pointer.fk.L"
        pointer2fkl = "finger.pointer2.fk.L"
        pointer3fkl = "finger.pointer3.fk.L"
        pointerikl = "finger.pointer.ik.L"
        pointerl_group = [pointerfkl, pointer2fkl, pointer3fkl, pointerikl]
        if isSelected(pointerl_group):
            layout.prop(pose_bones["finger.pointer.ik.L"], '["pointer.L fk_ik"]', slider=True)

        pointerfkr = "finger.pointer.fk.R"
        pointer2fkr = "finger.pointer2.fk.R"
        pointer3fkr = "finger.pointer3.fk.R"
        pointerikr = "finger.pointer.ik.R"
        pointerr_group = [pointerfkr, pointer2fkr, pointer3fkr, pointerikr]
        if isSelected(pointerr_group):
            layout.prop(pose_bones["finger.pointer.ik.R"], '["pointer.R fk_ik"]', slider=True)
        
        middlefkl = "finger.middle.fk.L"
        middle2fkl = "finger.middle2.fk.L"
        middle3fkl = "finger.middle3.fk.L"
        middleikl = "finger.middle.ik.L"
        middlel_group = [middlefkl, middle2fkl, middle3fkl, middleikl]
        if isSelected(middlel_group):
            layout.prop(pose_bones["finger.middle.ik.L"], '["middle.L fk_ik"]', slider=True)
        
        middlefkr = "finger.middle.fk.R"
        middle2fkr = "finger.middle2.fk.R"
        middle3fkr = "finger.middle3.fk.R"
        middleikr = "finger.middle.ik.R"
        middler_group = [middlefkr, middle2fkr, middle3fkr, middleikr]
        if isSelected(middler_group):
            layout.prop(pose_bones["finger.middle.ik.R"], '["middle.R fk_ik"]', slider=True)
        
        ringfkl = "finger.ring.fk.L"
        ring2fkl = "finger.ring2.fk.L"
        ring3fkl = "finger.ring3.fk.L"
        ringfikl = "finger.ring.ik.L"
        ringl_group = [ringfkl, ring2fkl, ring3fkl, ringfikl]
        if isSelected(ringl_group):
            layout.prop(pose_bones["finger.ring.ik.L"], '["ring.L fk_ik"]', slider=True)
        
        ringfkr = "finger.ring.fk.R"
        ring2fkr = "finger.ring2.fk.R"
        ring3fkr = "finger.ring3.fk.R"
        ringfikr = "finger.ring.ik.R"
        ringr_group = [ringfkr, ring2fkr, ring3fkr, ringfikr]
        if isSelected(ringr_group):
            layout.prop(pose_bones["finger.ring.ik.R"], '["ring.R fk_ik"]', slider=True)
        
        pinkyfkl = "finger.pinky.fk.L"
        pinky2fkl = "finger.pinky2.fk.L"
        pinky3fkl = "finger.pinky3.fk.L"
        pinkyikl = "finger.pinky.ik.L"
        pinkyl_group = [pinkyfkl, pinky2fkl, pinky3fkl, pinkyikl]
        if isSelected(pinkyl_group):
            layout.prop(pose_bones["finger.pinky.ik.L"], '["pinky.L fk_ik"]', slider=True)
        
        pinkyfkr = "finger.pinky.fk.R"
        pinky2fkr = "finger.pinky2.fk.R"
        pinky3fkr = "finger.pinky3.fk.R"
        pinkyikr = "finger.pinky.ik.R"
        pinkyr_group = [pinkyfkr, pinky2fkr, pinky3fkr, pinkyikr]
        if isSelected(pinkyr_group):
            layout.prop(pose_bones["finger.pinky.ik.R"], '["pinky.R fk_ik"]', slider=True)
        
        
### Rig Layers
class RigLayers(bpy.types.Panel):
    bl_label = "Rig Layers"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        
        # head
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=0, toggle=True, text='head')
        
        # eyes
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=7, toggle=True, text='eye')
        row.prop(context.active_object.data, 'layers', index=23, toggle=True, text='eyeball tweaks')
        
        # torso
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=1, toggle=True, text='torso')
        row.prop(context.active_object.data, 'layers', index=17, toggle=True, text='torso tweaks')
        
        # left arm
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=2, toggle=True, text='fk arm.l')
        col2 = row.column()
        col2.prop(context.active_object.data, 'layers', index=3, toggle=True, text='fk>ik')
        col2.prop(context.active_object.data, 'layers', index=2, toggle=True, text='ik>fk')
        row.prop(context.active_object.data, 'layers', index=3, toggle=True, text='ik arm.l')
                
        # right arm
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=18, toggle=True, text='fk arm.r')
        col2 = row.column()
        col2.prop(context.active_object.data, 'layers', index=19, toggle=True, text='fk>ik')
        col2.prop(context.active_object.data, 'layers', index=18, toggle=True, text='ik>fk')
        row.prop(context.active_object.data, 'layers', index=19, toggle=True, text='ik arm.r')
        
        # fingers
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=4, toggle=True, text='fk fingers')
        row.prop(context.active_object.data, 'layers', index=20, toggle=True, text='ik fingers')
        
        # left leg
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=5, toggle=True, text='fk leg.l')
        col2 = row.column()
        col2.prop(context.active_object.data, 'layers', index=6, toggle=True, text='fk>ik')
        col2.prop(context.active_object.data, 'layers', index=5, toggle=True, text='ik>fk')
        row.prop(context.active_object.data, 'layers', index=6, toggle=True, text='ik leg.l')
        
        # right leg
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=21, toggle=True, text='fk leg.r')
        col2 = row.column()
        col2.prop(context.active_object.data, 'layers', index=22, toggle=True, text='fk>ik')
        col2.prop(context.active_object.data, 'layers', index=21, toggle=True, text='ik>fk')
        row.prop(context.active_object.data, 'layers', index=22, toggle=True, text='ik leg.r')
        
        # root
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=16, toggle=True, text='ROOT')
    
bpy.utils.register_class(RigUI)
bpy.utils.register_class(RigLayers)