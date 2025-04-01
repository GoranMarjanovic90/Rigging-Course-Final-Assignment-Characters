# 🦴 Character Rigging - Final Assignment

This is my final rigging project for the **Rigging Course**. It shows a full rig setup created from scratch in Autodesk Maya. It has been so fun and so challenging.

---

## 🎯 Project Goals

- Build a production-ready, clean rig for a humanoid character.
- Provide full **FK/IK functionality** with switching systems.  
- Implement **constraint-based blending** between IK and FK joints.  
- Ensure **proper skinning**.
- Automate rig creation tasks using **Python scripting**.
- Organize outliner and naming conventions.

---

## ✅ Features

- **IK and FK controls** for arms and legs.  
- **Pole vector controls** for elbows and knees.  
- **FK/IK switch system**.
- **Blend joints system** for clean deformation and control separation.  
- **Constraint hierarchy** to isolate control systems.
- **Clean scene setup**: deleted history, frozen transforms, centered pivots.  
- **Zeroed-out controls** for animation readiness.

---

## 🧩 Key Technical Components

### FK/IK Systems

- Each limb has duplicate chains: one for FK, one for IK.  
- Blend joints are driven via constraints from both chains.  
- Pole vector controls are added

### Constraint Workflow

- `parentConstraint` and `poleVectorConstraint` nodes drive the blend system.  
- Python scripts check for existing constraints and avoid duplicates.  
- All connections can be re-evaluated or rebuilt.

### Skinning & Deformation

- This ensures IK/FK switching doesn’t break the deformation.  
- Root and spine joints are included in the skin cluster.  
- Skin weights can be transferred and edited non-destructively.

---

## 🧠 Learning Outcomes

From this project, I gained experience in:

- Automating rigging with Python in Maya.  
- Building IK/FK switch systems.  
- Managing scene hierarchy and joint structures.  
- Preparing a rig for animation and skinning pipelines.  

---

## 🧼 Final Notes

- All nodes are named with clear, consistent conventions.  
- The rig was tested for animation stability.  
- Every part of the rig can be regenerated with scripts.  
- Future upgrades can include a GUI-based IK/FK switch or controller visibility toggles.

---

## 🙏 Acknowledgements

Thanks to my instructor Gabriel Betros for feedback and support during the rigging course and annoyingness pushed me to level up and stay persistent through all the rigging chaos.

---

Made in Maya using Python and a lot of `cmds.parentConstraint()` magic 💪
